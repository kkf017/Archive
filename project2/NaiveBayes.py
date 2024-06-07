import numpy

# https://levelup.gitconnected.com/classification-using-gaussian-naive-bayes-from-scratch-6b8ebe830266

# https://www.kaggle.com/code/gautigadu091/gaussian-naive-bayes-from-scratch-in-python


# https://medium.com/@wanigathungasasini/an-in-depth-exploration-of-na%C3%AFve-bayes-from-theory-to-implementation-in-python-c11622f88677

# Gaussian for : discrete, continuous, discrete/continuous

class GaussianNaiveBayes():
	def __init__(self,):
		pass
	
	def fit(self, X_train, y_train):
		print(f"fit - {X_train.shape}, {y_train.shape}")
		
		y = numpy.unique(y_train)
		print(f"y - {y}")
	

		# P( Y = y | {x₁,x₂,x₃,x₄}) is proportional to P({x₁,x₂,x₃,x₄} | y )*P(y)
		# P( Y = y | {x₁,x₂,x₃,x₄}) ~ P(x1 | y) P(x2 | y) P(x3 | y) ... P(y)
	
		
		#  prob of each label
		Py = {} 
		gy = {} # {class0 : (mean0, sigma0), class1 : (mean1, sigma1) ...}
		for yi in numpy.unique(y_train):
			sample = y_train[numpy.where(y_train==yi)]
			mean = numpy.mean(sample)
			sigma = numpy.std(sample)
			py = sample.shape[0] / y_train.shape[0]
			Py[yi] = py
			gy[yi] = (mean, sigma)
			
		print(f"\n{Py}")
	
		Px = numpy.zeros(X_train.shape[0], y_train.shape[0])
		# prob - P(Xi | y)
		
	def predict(self, X_test, y_test):
		pass
