library(tidyverse)
library(dplyr)

# Code for data generation

#set thresholds
threshold<-c(5000,10000,15000,20000,25000,30000,35000,40000,45000,50000)


#Dataset 1 - equal gender split and salary drawn from the same distrubution. Default based on a simple thershold rule
dataset_1_i<-data.frame(gender=sample(rep(c("female","male"),times=c(500,500)),1000),salary=round(rnorm(1000,mean=29000,sd=10000)))

dataset_1<-data.frame()
for(i in threshold){
  data<-dataset_1_i%>%mutate(default=as.integer(salary<=i),thres=i)
  dataset_1<-rbind(dataset_1,data)
}

#Dataset 2- equal gender split but salary drawn from different distributions. Default based on a simple threshold rule
df_1<-data.frame(gender=sample(rep(c("female"),times=c(500)),500),salary=round(rnorm(500,mean=20000,sd=10000)))
df_2<-data.frame(gender=sample(rep(c("male"),times=c(500)),500),salary=round(rnorm(500,mean=38000,sd=10000)))
dataset_2_i<-rbind(df_1,df_2)
dataset_2<-data.frame()
for(i in threshold){
  data<-dataset_2_i%>%mutate(default=as.integer(salary<=i),thres=i)
  dataset_2<-rbind(dataset_2,data)
}


#Dataset 3- different gender split and salary drawn from different distributions. Default based on a simple threshold rule
df_1<-data.frame(gender=sample(rep(c("female"),times=c(250)),250),salary=round(rnorm(250,mean=20000,sd=10000)))
df_2<-data.frame(gender=sample(rep(c("male"),times=c(750)),750),salary=round(rnorm(750,mean=38000,sd=10000)))
dataset_3_i<-rbind(df_1,df_2)
dataset_3<-data.frame()
for(i in threshold){
  data<-dataset_3_i%>%mutate(default=as.integer(salary<=i),thres=i)
  dataset_3<-rbind(dataset_3,data)
}

#Dataset 1 n - Similar properties to Dataset 1 but default has a stochastic 
#component. For females that have defaulted by the simple threshold rule half of
#them will not default according to the new rule
set.seed(5)
p<-0.5
data_test<-dataset_1%>% filter(gender=="female")

data_test_n<-data_test
for (i in 1:nrow(data_test)){
  if (data_test[i,2]<=data_test[i,4]){
    if(runif(1)<=p){
      data_test_n[i,3]<-0
    }
    else{
      data_test_n[i,3]<-1
    }
  }
  else{
    data_test_n[i,3]<-0
  }
}

bb<-dataset_1%>%filter(gender=="male")

dataset_1_n<-rbind(data_test_n,bb)

#Dataset 2 n - Similar properties to Dataset 2 but default has a stochastic 
#component. For females that have defaulted by the simple threshold rule half of
#them will not default according to the new rule
set.seed(5)
p<-0.5
data_test<-dataset_2%>% filter(gender=="female")

data_test_n<-data_test
for i in range
  if (<=data_test[i,4]){
    if(runif(1)<=p){
      data_test_n[i,3]<-0
    }
    else{
      data_test_n[i,3]<-1
    }
  }
  else{
    data_test_n[i,3]<-0
  }
}

bb<-dataset_2%>%filter(gender=="male")

dataset_2_n<-rbind(data_test_n,bb)

#Dataset 3 n - Similar properties to Dataset 3 but default has a stochastic 
#component. For females that have defaulted by the simple threshold rule half of
#them will not default according to the new rule
set.seed(5)
p<-0.5
data_test<-dataset_3%>% filter(gender=="female")


data_test_n<-data_test
for (i in 1:nrow(data_test)){
  if (data_test[i,2]<=data_test[i,4]){
    if(runif(1)<=p){
      data_test_n[i,3]<-0
    }
    else{
      data_test_n[i,3]<-1
    }
  }
  else{
    data_test_n[i,3]<-0
  }
}

bb<-dataset_3%>%filter(gender=="male")

dataset_3_n<-rbind(data_test_n,bb)

#outputting datasets into files
write.table(dataset_1,file='dataset_1')
write.table(dataset_2,file='dataset_2')
write.table(dataset_3,file='dataset_3')

write.table(dataset_1_n,file='dataset_1_n')
write.table(dataset_2_n,file='dataset_2 _n')
write.table(dataset_3_n,file='dataset_3_n')

