# ProjectGroup-14

# First proposal

**Project Title**  
Sound Profound !
(Urban Sound Classification and its response to gunshot sound using the implementation of Deep Neural Networks)

**Project Idea Description**  
From the past few years, this has been observed that Artificial Intelligence has progressed into the medium of sound also. This idea has been taken and the implementation is to classify and identify maximum possible urban sounds. This will be done by utilizing the difference in frequency, intensity and wavelength. It can be used to plot a spectrograph and a mel-spectrogram would be utilized to identify the pattern of sound. The major aspect here is to identify the gunshot sound and report it immediately to the concerned authorities for quick action.

**Goals of the project**  
To classify and identify the urban sounds and take immediate action on hearing the gunshot sound. The intention of this project is to support the police department to take a quick action in case of emergency situations. This would inturn reduce the time of action of the police and inturn increase their job efficiency in terms of time, catching hold of the criminal.

**Abstract**  
Artificial Intelligence has already progressed into many areas and in the past few years it has advanced into the medium of sound. It can be the generation of a sound or identification of it. The problem of automatic environmental sound classification has received increasing attention from the research community in recent years. Its applications range from context aware computing and surveillance to noise mitigation enabled by smart acoustic sensor networks.

To overcome this, a variety of signal processing and machine learning has been applied to it. This includes matrix factorization, dictionary learning, wavelet filter-banks and most recently deep neural networks.

In this project we would attempt to distinguish between the different environmental sounds by using deep convolutional neural networks. The rationale behind the use is to mitigate a major challenge which is distinguishing between two overlapping sounds. Environmental sound usually are difficult to detect since on most of the occasion the sounds are overlapped by noises which are in turn also one of the sounds of interest, for e.g., sound of dogs barking overlapped by revving engine. Deep convolutional neural networks provides us with an advantage of capturing energy modulation patterns across time and frequency when applied to spectrogram-like inputs, which has been shown to be an important trait for distinguishing between different noise like sounds such as jack-hammer and air-conditioner. With this, the next pace is to take action on the gunshot sound once it has been labelled. The design implementation would be such that would inform the concerned authorities with an immediate effect.


**Technology Stack**
* 	Deep CNN to classify the sound.
* 	Log scaled mel-spectrogram to observe time frequency patches.
* 	Python 
* 	Keras
* 	Librosa for analysis of audio signals.




# Second proposal

**Project Title** <br />
Still good or Stale! 

 **Goal** <br />
To reduce food wastage due to the expiration of perishable food. 

**Abstract**<br />
With the advent of increase in population, the food wastage has become a global crisis. As a fact in US alone “40 percent of food gets tossed every year—and that amounts to $162 billion in waste annually, according to the Natural Resources Defense Council.” Many researchers and environmentalists are trying to figure out the best methods to reduce the food wastage. Either by spreading awareness about food wastage or by building a tool to track and reduce the food wastage. Our product aims to do so by the second approach, i.e. by providing a tool to track the life span of food products when refrigerated. As one of the main contributors to the food wastage is the inability to track when the food starts to stale. 

**Description**<br />
The project intends to keep track of the refrigirated fresh produce and help consume them before they begin to rot. After the user shops for fresh produce or diary product, he uploads a picture of the invoice. Using text recognition achived through machine learning with the help of IBM Watson, the application identifies the fresh produce in the grocery bag and their shelf life after they are refrigirated. For instance if the user had shopped for carrots and eggplants, the application adentifies the approximate shelf life of carrots and eggplant when refrigirated. After the shelf life is identified as n days, the application prompts the user to utilise the items in n/2 days. In the example here shelf life of carrot is 21 days and that of eggplant is 7 days, after 3 days the application notifies the user to consume the eggplant if not already done and also suggests a few recipies which include eggplant and any other vegetable or fresh produce present, like here carrots. After the completion of n days, the application prompts the user to discard the foos product as it has become stale. The user can additionally login to the application to manipulate the items in his list.

**Hill Statement** 
* **Who** Common people who buy groceries but are unable to track when it begins to stale. <br />
* **What** Alert them with the upcoming expiration of their perishable food.

**Technology Stack (Tentative)**
* **Programming languages & Libraries:** Python. <br />
* **Tools & Technologies:** Machine Learning, IBM Watson, Cloud for deployment <br />
* **Web Technologies:** HTML5, CSS3, JavaScript, React, REST API


# Third proposal

**Project Title** <br />
Greet and Treat

**Goal** <br />
To classify and provide appropriate results, when a user implements certain inputs, based on his symptoms. The application, would provide possible list of  illness, allergies, infections prioritized based not just on symptoms, but also on the location the user is situated in, so that it could warn the user about specific epidemics that have similar symptoms prominent in the area.

**Abstract**<br />
Cognitive Computing is an upcoming field in Computer Science and cognitive systems are generated to mimic the human thought process by accepting natural language inputs and processing it with the help of machine learning techniques. These systems interact with each other and help humans to gain insights of the data. IBM Watson is an example of such cognitive question-answering system, which is capable of handling natural language questions asked by the users. IBM Watson accepts questions expressed in natural language by users and seeks to understand it to return appropriate result. It immediately retrieves suggestions for user’s questions. We make use of IBM Watson in this project to take multiple symptoms from the user and it would give results on what could possible be the illness.
While Cognitive Computing has now began its advancement in the feild of Medicine, we intend to provide users with an application that can provide them with possible illness/allergies/infections based on the symptoms entered by the user. Using IBM Watson, we use the huge datasets available on the internet to give appropriate results.

**Description**<br />
The field of cognitive computing is one of the most interesting researches going on currently. With this project,we use the concept of cognitive computing system on IBM Watson, to learn and interpret data. Cognitive computing system use various concepts of Natural Language Processing(NLP) and Machine Learning(ML) for the purpose of developing patterns within the data and build their own learning structures to answer questions they are asked accurately, which is what we intend to implement so user can easily get access to medical information such as illness, allergies, infections, etc which could be filtered based on geographic locations as well, to give warnings on specific location epidemics.

**Technology Stack (Tentative)**
* **Programming languages & Libraries:** Python <br />
* **Tools & Technologies:** IBM Watson, Natural Language Processing and Machine Learning
