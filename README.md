
ResNet-50 Model for Aquarium Marine Fish Classification
This repository contains a ResNet-50 model implemented using Python and PyTorch for the purpose of classifying aquarium marine fish.
The model is trained to accurately identify and classify different species of marine fish commonly found in aquarium settings. Additionally, a Flask web application has been deployed to provide an interactive interface for users to classify images of marine fish.

Dataset
The dataset used for training and evaluation consists of a large collection of high-resolution images of various marine fish species.
The images were carefully curated and labeled with their respective species for supervised learning.

Model Architecture
The ResNet-50 architecture was chosen for its exceptional performance in image classification tasks. 
It is a deep convolutional neural network (CNN) model that utilizes residual connections to overcome the vanishing gradient problem and enable effective training of deeper networks. 
The model's architecture consists of 50 layers, including convolutional layers, residual blocks, and fully connected layers, allowing it to learn complex features and patterns from the input images.

Training
The model was trained using a supervised learning approach. 
The dataset was split into training and validation sets to monitor the model's performance during training and prevent overfitting. 
The training process involved optimizing the model's parameters using stochastic gradient descent (SGD) with momentum. The learning rate was adjusted dynamically using a learning rate scheduler to improve convergence.

Evaluation
The trained ResNet-50 model was evaluated using the validation set to assess its classification accuracy and generalization capabilities. Performance metrics such as accuracy, precision, recall, and F1 score were calculated to measure the model's effectiveness in classifying marine fish species.

Flask Web Application
To provide a user-friendly interface for image classification, a Flask web application has been developed and deployed. 
Users can upload their images of marine fish to the application, which utilizes the trained ResNet-50 model to classify the fish species. The application provides real-time predictions and displays the predicted species along with a confidence score.
