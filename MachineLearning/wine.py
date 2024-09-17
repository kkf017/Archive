import numpy

from sklearn import datasets

from NaiveBayes import GaussianNaiveBayes

from typing import List, Tuple, Dict


DATASET = datasets.load_wine()


def split(X:numpy.ndarray, y:numpy.ndarray, sample:int, percent:float)->Tuple[numpy.ndarray]:

	ntest = int(percent*sample)
	ntrain = sample - ntest 

	train = numpy.array([])
	test = numpy.array([])

	for i in numpy.unique(y):
		a = y[numpy.where(y==i)]

		index = numpy.copy(numpy.where(y==i))
		index = numpy.reshape(index, (index.shape[1],))
		numpy.random.shuffle(index)

		train = numpy.concatenate((train, index[:ntrain]))
		test = numpy.concatenate((test, index[ntrain:ntrain+ntest]))

	train = train.astype(numpy.int32)
	test = test.astype(numpy.int32)
	return X[train], y[train], X[test], y[test]



if __name__=="__main__":

	data = datasets.load_wine() #Odata_home="~/Documents/project/sklearn-data")

	print(f"\033[0;35mDataset\033[0m: {data.data.shape}")
	print(f"\033[0;35mFeatures\033[0m: {data.feature_names}")
	print(f"\033[0;35mLabels\033[0m: {numpy.unique(data.target)}")

	X = numpy.copy(data.data)
	print(f"\nX: {X.shape}")

	y = numpy.copy(data.target)
	print(f"y: numpy.unique(y)")

	print(f"\n")
	for i in numpy.unique(y):
		x = numpy.copy(X[numpy.where(y == i)])
		print(f"{i}, {x.shape}")


	X_train, y_train, X_test, y_test = split(X, y, 48, 0.33)
	print(f"\nTrain: {X_train.shape} {y_train.shape}")
	print(f"Test: {X_test.shape} {y_test.shape}")
	
	model = GaussianNaiveBayes()
	model.fit(X_train, y_train)
