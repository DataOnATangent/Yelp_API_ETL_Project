# Flatiron School Phase 1 Project
Yelp API Based Project 

Overview:
======
This project seeks to identify the best location for a new business providing spa services using the data available through the Yelp API. 

## Business Problem: 

<p align="center">
  <img width="460" height="300" src=Images/yelp_logo.png>
</p>
We are looking to open a new spa, Hasta Spa Vista, and trying to decide where is the best geographical area for it. The spa industry is set firmly in the realm of luxury non-essential, as such we chose to look at a location that we felt would be amenable to this kind of business. Florida, being exempt from state tax, having multiple tourist destinations, and being home to the largest population or retirees was an obvious choice within. As a new business looking to save money in the early stages of research, we have decided to use data from the Yelp API to make a choice between the metro areas of Miami and Orlando.  

## Analysis Focus
1. The analysis focuses on one thousand businesses within a 25 miles radius of the Miami metro area city center and Orlando metro area city center. 
2. Using the available data from the Yelp API to identify the difference between these two locations to indicate the location with a higher chance of sustaining a new spa.  

## Analysis 

### Initial Findings 

We began our analysis by looking at the available datapoint of price tier, rating, business density, categories, zip-code, and review count. Notably, throughout our analysis, if any of these points were unavailable the business was excluded from that aspect of the analysis. What we discovered early on was how highly analogous our chosen markets are. 


<p align="center">
  <img width="260" height="250" src=Images/Area_Business_By_Price_Tier.png>
<img width="260" height="230" src=Images/Area_Business_By_Rating.png>
    <img width="260" height="400" src=Images/Area_Business_By_Review_Count.png>
</p>   

Specifically, when it came to rating distribution, price tier distribution, and review counts, the difference between the two were negligible. While this would mean we would need to dig a little deeper to form a basis for our location decision, it did mean that both locations were comparatively good options for a new business. 
<p align="center">
  <img width="660" height="450" src=Images/Area_Combined_Rating_By_Price_count.png>
</p> 

Both locations already support a high density of spas with more than 1500 hundred spas within 25 miles of the city center and a multitude of categories. 

<p align="center">
   <img width="460" height="400" src=Images/Area_Business_Catagory.png>
</p> 


### Limitations

This also highlighted the limitations of working with Yelp data as further outside research was required for what was intended as a prefatory inquiry. Upon bringing in median income data from incomebyzip.com we discovered that while Miami had income outliers that made its upper range higher ($170,673 vs $105,833) , Orlando's median was substantially higher ($51,757 vs $39,049). 

### Digging Deeper 

We next chose to focus to look at which zip-codes had the highest density of spas believing that if these zip-codes already supported a high number of similar businesses, these areas would also be reflective of our future customers.


<p align="center">
  <img width="460" height="300" src=Images/Miami_Zip_density.png>
<img width="460" height="300" src=Images/Orlando_Zip_Density.png>
</p>

And thus, we decided to repeat our analysis using the top five densest zip-codes for each area. Upon doing so we discover that these zip-code all had a higher median income versus the larger metro area. 

 <p align="center">
  <img width="460" height="300" src=Images/Zip_median_income_miami.png> 
    <img width="460" height="300" src=Images/Zip_median_income_orlando.png>
</p>

This is where we started to note differences including room for growth in the high tier market.  

 
<p align="center">
  <img width="660" height="300" src=Images/Zip_rating_by_price_tier_count_2.png>
</p> 


Moreover when looking at review count for by price tier, the subset further highlights the room for growth as compared to Miami because people due to stark difference in number of reviews.  

 <p align="center">
  <img width="460" height="500" src=Images/Zip_review_count_boxplot.png>
</p> 

## Summary 
- Miami and Orlando are very similar metro areas, which both currently support a bustling spa industry. 

- However, while both locations show opportunity for market growth in the high-end tier of the spa market, Orlando's higher average median income makes it a more viable option to open a new business.

## Repository Structure  
All data sets can be found in /data folder. All plots and locally saved images can be found in /images folder. 

## Presentation
Presentation Deck(LINK HERE)

## Contributors 
[Dariga Kokenova](https://github.com/darigak)
[Jiji Craynock](https://github.com/DataOnATangent) 
