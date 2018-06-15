train <- read.csv ( "G:/Local disk/MachineLearning/Data_Processing/convolutional_network/train.csv")
# Create a 28*28 matrix with pixel color values
m = matrix(unlist(train[10,-1]), nrow = 28, byrow = TRUE)
par(mar = rep(2, 4))
# Plot that matrix
image(m,col=grey.colors(255))

# reverses (rotates the matrix)
rotate <- function(x) t(apply(x, 2, rev)) 

# Plot some of images
par(mfrow=c(2,3))
lapply(1:6, 
       function(x) image(
         rotate(matrix(unlist(train[x,-1]),nrow = 28, byrow = TRUE)),
         col=grey.colors(255),
         xlab=train[x,1]
       )
)

par(mfrow=c(1,1)) # set plot options back to default
library (caret)
inTrain<- createDataPartition(train$label, p=0.8, list=FALSE)
training<-train[inTrain,]
testing<-train[-inTrain,]

#store the datasets into .csv files
write.csv (training , file = "G:/Local disk/MachineLearning/Data_Processing/convolutional_network/train-data.csv", row.names = FALSE) 
write.csv (testing , file = "G:/Local disk/MachineLearning/Data_Processing/convolutional_network/test-data.csv", row.names = FALSE)
library(h2o)
# 
# #start a local h2o cluster
# local.h2o <- h2o.init(ip = "localhost", port = 54321, startH2O = TRUE, nthreads=-1)
# training <- read.csv ("G:/Local disk/MachineLearning/Data_Processing/convolutional_network/train-data.csv") 
# testing  <- read.csv ("G:/Local disk/MachineLearning/Data_Processing/convolutional_network/test-data.csv")
# 
# # convert digit labels to factor for classification
# training[,1]<-as.factor(training[,1])
# 
# # pass dataframe from inside of the R environment to the H2O instance
# trData<-as.h2o(training)
# tsData<-as.h2o(testing)
# res.dl <- h2o.deeplearning(x = 2:785, y = 1, trData, activation = "Tanh", hidden=rep(160,5),epochs = 20)
# #use model to predict testing dataset
# pred.dl<-h2o.predict(object=res.dl, newdata=tsData[,-1])
# pred.dl.df<-as.data.frame(pred.dl)
# 
# summary(pred.dl)
# test_labels<-testing[,1]
# 
# #calculate number of correct prediction
# sum(diag(table(test_labels,pred.dl.df[,1])))
# # read test.csv
# test<-read.csv("test.csv")
# 
# test_h2o<-as.h2o(test)
# 
# # convert H2O format into data frame and save as csv
# df.test <- as.data.frame(pred.dl.test)
# df.test <- data.frame(ImageId = seq(1,length(df.test$predict)), Label = df.test$predict)
# write.csv(df.test, file = "submission.csv", row.names=FALSE)
# 
# # shut down virtual H2O cluster
# h2o.shutdown(prompt = FALSE)