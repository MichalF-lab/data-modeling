library(MASS)

n<-10
x<-1:n/2
beta<-c(10,3,2)
sigma<-1/2
eps<-rnorm(n,0,sigma)
y<-beta[1]*x/(beta[2]+x)+beta[3]+eps

g<-function(x,b1,b2,b3){
  return(b1*x/(b2+x)+b3)}

gradient<-function(x,b1,b2,b3){
  g1<-x/(b2+x)
  g2<- -b1*x/(b2+x)^2
  g3<-1
  return(c(g1,g2,g3))}

G.j<-function(x,b1,b2,b3){
  n<-length(x)
  G<-matrix(rep(0,n*3),ncol=3,nrow=n)
  for (i in 1:n){
    G[i,]<-gradient(x[i],b1,b2,b3)}
  return(G)}

beta.j<-function(x,y,b1,b2,b3){
  beta<-matrix(c(b1,b2,b3),ncol=1,nrow=3)
  G<-G.j(x,b1,b2,b3)
  Y<-matrix((y-g(x,b1,b2,b3)),ncol=1,nrow=length(y))
  beta.nowe<-beta+ginv(t(G)%*%G)%*%t(G)%*%Y
  return(beta.nowe)}

wiarogodność<-function(x,y,b1,b2,b3,sigma){
  n<-length(y)
  return(-n/2*(log(2*pi*sigma))-sum((y-g(x,b1,b2,b3))^2)/2/sigma)}

Gauss.Newtonn<-function(x,y,b1,b2,b3,M=100,epsilon=0.0001){
  n<-length(y)
  sigma<-sum((y-g(x,b1,b2,b3))^2)/(n-3)
  tabelka<-matrix(c(b1,b2,b3,sigma,
          wiarogodność(x,y,b1,b2,b3,sigma)),ncol=5,nrow=1)
  beta<-matrix(c(b1,b2,b3),ncol=1,nrow=3)
  for (i in 1:M){
    beta.n<-beta.j(x,y,beta[1],beta[2],beta[3])
    sigma<-sum((y-g(x,beta.n[1],beta.n[2],beta.n[3]))^2)/(n-3)
    L<-wiarogodność(x,y,beta.n[1],beta.n[2],beta.n[3],sigma)
    tabelka<-rbind(tabelka,c(beta.n,sigma,L))
    if (sum((beta-beta.n)^2)<=epsilon^2){
      return(tabelka)}
    beta<-beta.n}
  return(tabelka)}
