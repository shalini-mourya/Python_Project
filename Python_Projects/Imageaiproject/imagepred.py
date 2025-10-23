from imageai.Classification import ImageClassification
import os
execution_path = os.getcwd()

prediction=ImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path,"densenet121-a639ec97.pth"))
prediction.loadModel()

prediction, probabilities = prediction.classifyImage(os.path.join(execution_path,"godzilla.jpg"),result_count=5)
for eachPrediction, eachProbabilitiy in zip(prediction, probabilities):
	print(eachPrediction, ":", eachProbabilitiy)