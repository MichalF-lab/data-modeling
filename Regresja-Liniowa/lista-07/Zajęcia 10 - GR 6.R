set.seed(123)
n<-300
p<-20
X<-matrix(rnorm(n*p,2,5),ncol=p,nrow=n)
X[,1]<-rep(1,n)
beta<-c(rnorm(10,0,1/4),numeric(10))
pi.p<-1/(1+exp(-X%*%beta))
colnames(X)<-sapply(1:p,function(i){paste0("X",i)})
dane<-data.frame(X)
dane$Y<-rbinom(n,1,pi.p)
write.csv(dane,"daneG5.csv",row.names=F)

id.0<-which(dane$Y==0)
id.1<-which(dane$Y==1)

train.0<-sample(id.0,size=floor(0.7*length(id.0)))
train.1<-sample(id.1,size=floor(0.7*length(id.1)))

id.train<-sort(c(train.0,train.1))
id.test<-setdiff(seq_len(n),id.train)

train<-dane[id.train,]
test<-dane[id.test,]

#mean(train$Y)
#mean(test$Y)

model.full<-glm(Y~.,data=train[,-1],family=binomial)
model.null<-glm(Y~1,data=train[,-1],family=binomial)

anova(model.null,model.full,test='LRT')  

confint(model.full)

summary(model.full)

cbind(beta,coef(model.full))

coef(model.full)[2]

exp(coef(model.full))[2]

pred.test<-predict(model.full,
                   newdata=test,type='response')

wskaźniki<-function(poziom=0.5){
  pred.class<-ifelse(pred.test>poziom,1,0)
  cm<-table(pred=pred.class,real=test$Y)
  sen<-cm[2,2]/sum(cm[,2])
  spec<-cm[1,1]/sum(cm[,1])
  fpr<-cm[2,1]/sum(cm[,1])
  fnr<-cm[1,2]/sum(cm[,2])
  acc<-sum(diag(cm))/sum(cm)
  miary<-c(sen,spec,fpr,fnr,acc)
  names(miary)<-c("sen","spec","fpr","fnr","acc")
  return(list(cm=cm,miary=miary))
}

M.1<-wskaźniki(0.5)
M.2<-wskaźniki(0.7)

cbind(M.1$miary,M.2$miary)

library(pROC)
roc.obj<-roc(test$Y,pred.test)
auc(roc.obj)
plot(roc.obj,col='red')
