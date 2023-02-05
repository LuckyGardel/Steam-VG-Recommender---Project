# Steam-VG-Recommender_Project

#### BUILDING A VIDEOGAMES RECOMMENDER BASED ON STEAM PLATFORM

The purpose of this project is to build a videogames recommendation app capable of returning 10 similar results as the one which the user inputs in the serach tab. 


#### BACKGROUND AND DATA

Background:

Steam is the biggest videogames platform in the world. It currently haves more than 50k games in its portfolio.   

I am going to build a recommender based on different similarities analyzed and deducted from the data after: 

        Scraping the Steam Store  
        EDA - Selection and Cleaning of features
        Building the recommendation app
        Testing the recommender
                
Data: 

I have chosen a dataset containing information about more than 40k games from Steam. 

The original dataset can be found here: https://www.kaggle.com/datasets/trolukovich/steam-games-complete-dataset

The other data used in the one that I scraped my own and you can see how it can be done in the folder Back_Code -> Scraping Steam Store

We end up with one DataSet resulting from the merge by name of the two previous ones. 

#### INFO OF THE REPOSITORY

. In Back_Code you have 3 different python books explaining the process step by step: 

    1. Scraping Steam Store: 
        
        We scrape the steam store website to obtain an updated list of the prices of different videogames of their porfolio
    
    2. Full-EDA :
        
        - Loading the dataset from Kaggle and our scraped data and merging them together
        - Standarizing headers
        - Cleaning and Dealing with duplicates and Nans
        - Selecting columns to build out recommender and more cleaning
        
    3. Building Recommender : 
    
        - Loading Final Data
        - Making the final selection of features
        - Modifying the data inside the columns as we need to 
        - Defining the Model (CountVectorizer)
        - Applying Cosine Similarity
        - Building recommender function
        
    4. Streamlit_app : 
    
        - The code to run the local env. to test the recommender 
        
 
 . In Summary_Ppt you will see a quick ppt used to present the recommender and containing the references and a video showing how the recommender performs. (Please find the video at the end of this file). 
         

#### CONCLUSIONS

. The result is a recommender built with python and presented in Streamlit, based on features such as the reviews from the users, the tags from the games 'ex,(FPS,Gore,Action,Demons,Shooter,First-Person...)', the details from the games 'ex, (Single-player,Multi-player,Co-op)' from more than 30 k games obtained from steam store.

. As you can see in the video below, after the user inputs the name of a game he likes in the search tab and clicks recommend, the app will spit 10 similar results with completely different prices so the user can click in the url next to it to go directly to the steam store, compare and enjoy. 

https://www.youtube.com/watch?v=2WI_MvEfooI
