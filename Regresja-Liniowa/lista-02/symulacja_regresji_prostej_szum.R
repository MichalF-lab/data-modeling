n <- 200
beta0 <- 1
beta1 <- 2

set.seed(123)

sigma <- 0.1
x <- runif(n, min = -2, max = 2)
epsilon <- rnorm(n, mean = 0, sd = sigma)
y <- beta0 + beta1 * x + epsilon

plot(x, y, main = "Chmura punktów (σ = 0.1)", 
     xlab = "x", ylab = "y", pch = 16, col = "blue")
grid()

xbar <- mean(x)
ybar <- mean(y)

beta1_hat <- sum((x - xbar) * (y - ybar)) / sum((x - xbar)^2)
beta0_hat <- ybar - beta1_hat * xbar

model1 <- lm(y ~ x)
summary(model1)

sigma_values <- c(0.1, 0.5, 1.0)
results <- data.frame(
  sigma = numeric(),
  beta0_hat = numeric(),
  beta1_hat = numeric(),
  R2 = numeric()
)

for (sig in sigma_values) {
  epsilon <- rnorm(n, mean = 0, sd = sig)
  y <- beta0 + beta1 * x + epsilon
  
  model <- lm(y ~ x)
  
  beta0_est <- coef(model)[1]
  beta1_est <- coef(model)[2]
  r2 <- summary(model)$r.squared
  
  results <- rbind(results, data.frame(
    sigma = sig,
    beta0_hat = beta0_est,
    beta1_hat = beta1_est,
    R2 = r2
  ))
}

print(results)

par(mfrow = c(1, 3))

for (i in 1:3) {
  sig <- sigma_values[i]
  set.seed(123)
  
  x <- runif(n, min = -2, max = 2)
  epsilon <- rnorm(n, mean = 0, sd = sig)
  y <- beta0 + beta1 * x + epsilon
  
  plot(x, y, main = paste("σ =", sig), 
       xlab = "x", ylab = "y", pch = 16, col = "blue", 
       ylim = c(-8, 8))
  
  model <- lm(y ~ x)
  abline(model, col = "red", lwd = 2)
  abline(a = beta0, b = beta1, col = "green", lwd = 2, lty = 2)
  
  legend("topleft", 
         legend = c("Linia regresji", "Rzeczywista linia"),
         col = c("red", "green"), 
         lty = c(1, 2), lwd = 2, cex = 0.8)
}

par(mfrow = c(1, 1))
