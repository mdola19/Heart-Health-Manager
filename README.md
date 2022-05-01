# Heart Stroke Manager
## Hackathon project for Hack::Peel 2022
According to the [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death) cardiovascular disease is the world's leading cause of death. More specifically, strokes are the 2nd leading cause of death globally. We wanted to create a project that helps tackle this issue. As a result, we created a web-app that uses Machine Learning to lower the risk of getting a stroke.


Full *Devpost* submission can be found at: [Devpost](https://devpost.com/software/heart-stroke-manager)


### Main Tools Used
- **HTML, CSS and JS** - Used to design the front end of the website.
- **Machine Learning** -  For the stroke prediction, we trained our very own machine learning model using [stroke data](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) on Kaggle. We then used a Jupyter Notebook and the Scikit Learn library to create the machine learning model. If interested, view the model training process [here](https://github.com/harsharan-r/Heart-Stroke-Manager/blob/master/Heart_Health_Website/Machine%20Learning%20Model/trainingstrokemodel.ipynb). 

- **SQL** - To store user data we created a SQL database which allows us to access user data from any file in a organized manner

- **Flask** - To integrate the machine learning model and the databases onto the website so it can interact with the Front End of the website, we used Flask. 

### How To Use
1. First download the repository
2. Now, run `main.py`
3. Go to: http://127.0.0.1:5000/
4. You should now be able to see the home page of the website
