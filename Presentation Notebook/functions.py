import requests
import json
import numpy as np

from  keys  import  client_id, api_key

headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }


def yelp_call(url, url_params, api_key):
    # code to make the yelp call for businesses
    response = requests.get(url, headers=headers, params=url_params)
    data = json.loads(response.text)
    return data
    
    
def parse_results(results, location):
    # code to parse the business results to make them easier to insert into the SQL business database
    parsed_results = []
    biz_ID_list = []

    for business in results['businesses']:
        for item in ['is_closed', 'review_count', 'categories', 'rating', 'price']:
            if item == 'categories':
                if len(business[item]) == 0:
                    business[item] = []
                    business[item].append({'alias': '', 'title': np.nan})
                    business[item].append({'alias': '', 'title': np.nan})
                elif len(business[item]) == 1:
                    business[item].append({'alias': '', 'title': np.nan})
            if item not in business:
                business[item] = np.nan
            else:
                business[item]

        biz_tuple = (business['id'], 
                business['name'] , 
                business['is_closed'], 
                business['review_count'],
                business['categories'][0]['title'], 
                business['categories'][1]['title'],
                business ['rating'], 
                business ['price'],
                location,
                business['location']['city'],
                business['location']['zip_code'])
        biz_ID_list.append(business['id'])
        parsed_results.append(biz_tuple)
    return parsed_results


def db_insert(cnx, cursor, parsed_results):
    # code to insert and commit the results to the SQL business database
    add_business = ("""INSERT INTO business 
              (id, name, is_closed, review_count, category_1, category_2, rating, price, area,
                   location_city, location_zipcode) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
    cursor.executemany(add_business, parsed_results)
    cnx.commit()
    
    
def yelp_review_call(business_id):
    # code to make the yelp call for reviews
    response = requests.get('https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id), headers=headers)
    review_data = json.loads(response.text)
    return review_data


def parse_review_results(review_results, business_id):
    # code to parse the review results to make them easier to insert into the SQL reviews database
    parsed_results = []
    
    if 'error' in review_results:
        if review_results['error']['code'] == 'BUSINESS_UNAVAILABLE': # to account for businesses without reviews
            return None
    else:
        for review in review_results['reviews']:
            for item in ['text', 'rating', 'time_created']:
                if item not in review:
                    review[item] = np.nan
                else:
                    review[item]

            review_tuple = (review['id'], 
                    review['text'] , 
                    review['rating'], 
                    review['time_created'],
                    business_id)
            parsed_results.append(review_tuple)
        return parsed_results
    

def db_review_insert(cnx, cursor, parsed_results):
    # code to insert and commit the results to the SQL review database
    add_review = ("""INSERT INTO reviews 
              (id, text, rating, time_created, business_id) 
              VALUES (?, ?, ?, ?, ?)""")
    cursor.executemany(add_review, parsed_results)
    cnx.commit()