# Feature engineering plan v01

04/22/2015

![image](https://www.evernote.com/shard/s54/sh/81ec5ae0-b5e5-43ad-8ce0-58bb41ef9b06/21f974462db97d585dac2400b715ab91/res/910bdc99-5eb3-4305-964d-a50f6709c442/skitch.png)

The number of features below is a little bit different from the picture above. F14-16 will be the last ones that we want to implement.  

## Features for User ID 
**F01. average response position (include positive and negative values all together)** *(Continuous)*

**F02. average response position using absolute values** *(Continuous)*

**F03. accuracy** *(Continuous)*

**F04. Clustering of UID based on...** *(Categorical)*

*First* implementation (2 vectors)

- average response position
- accuracy

*Second* implementation (12 x 2 vectors)

- average response for each category
- accuracy for each category

## Features for Question ID 
**F05. question length** *(Continuous)*

**F06. average response position (include positive and negative values all together)** *(Continuous)*

**F07. average response position using absolute values** *(Continuous)*

**F08. accuracy** *(Continuous)*

**F09. Clustering of QID based on...** *(Categorical)*

*First* implementation (2 vectors)

- average response position
- accuracy

*Second* implementation (12 x 2 vectors)

- average response for each category
- accuracy for each category

**F14. Median value of Proper Noun's position for each question** *(Continuous)*

It is unknown yet which one of these three features (F10, F11, F12) are going to be most helpful. We could choose only one feature among these three based on LASSO results. 

**F15. Mean value of Proper Noun's position for each question** *(Continuous)*

**F16. Mode value of Proper Noun's position for each question** *(Continuous)*

## Features for Caterogy ID 
**F10. Catergory ID** *(Categorical)*

**F11. average response position (include positive and negative values all together)** *(Continuous)*

**F12. average response position using absolute values** *(Continuous)*

**F13. accuracy** *(Continuous)*