"""
        ML Tools:
                - discrete vs. continuous
                - Naive Bayes, KNN, cluster, ... decision tree ... perceptron ... etc
                - PCA, FCA, LDA, EM, AR (AUto regressive models) ... Markov
                - deep learning 
                        -(...)
                
                #https://scikit-learn.org/stable/datasets.html
                
                # https://medium.com/analytics-vidhya/na%C3%AFve-bayes-algorithm-5bf31e9032a2
                # https://www.geeksforgeeks.org/naive-bayes-classifiers/
"""

"""
        Phishing
                - tool to send email 
                
        # https://softwareg.com.au/blogs/internet-security/how-to-make-a-firewall-in-python
        # https://www.youtube.com/watch?v=tbhYxd2sfAE&list=PLu9EF-eONbNilSwabagVqsD8hoPqWNUcE&index=6
"""



import random
import numpy

from sklearn import datasets


from typing import List, Tuple, Dict



DATASET = datasets.fetch_kddcup99

DISCRETE = ['protocol_type', 'service', 'flag', 'land', 'logged_in','root_shell', 'su_attempted','is_host_login','is_guest_login']
CONTINUOUS = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'urgent', 'hot','num_failed_logins','num_compromised', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files','num_outbound_cmds','count','srv_count','serror_rate','srv_serror_rate','rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate','srv_diff_host_rate', 'dst_host_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']

LABELS = {'duration': 0, 'protocol_type': 1, 'service': 2, 'flag': 3, 'src_bytes': 4, 'dst_bytes': 5, 'land': 6, 'wrong_fragment': 7, 'urgent': 8, 'hot': 9, 'num_failed_logins': 10, 'logged_in': 11, 'num_compromised': 12, 'root_shell': 13, 'su_attempted': 14, 'num_root': 15, 'num_file_creations': 16, 'num_shells': 17, 'num_access_files': 18, 'num_outbound_cmds': 19, 'is_host_login': 20, 'is_guest_login': 21, 'count': 22, 'srv_count': 23, 'serror_rate': 24, 'srv_serror_rate': 25, 'rerror_rate': 26, 'srv_rerror_rate': 27, 'same_srv_rate': 28, 'diff_srv_rate': 29, 'srv_diff_host_rate': 30, 'dst_host_count': 31, 'dst_host_srv_count': 32, 'dst_host_same_srv_rate': 33, 'dst_host_diff_srv_rate': 34, 'dst_host_same_src_port_rate': 35, 'dst_host_srv_diff_host_rate': 36, 'dst_host_serror_rate': 37, 'dst_host_srv_serror_rate': 38, 'dst_host_rerror_rate': 39, 'dst_host_srv_rerror_rate': 40}

DOS = [b'back.', b'land.', b'neptune.',b'pod.', b'smurf.',b'teardrop.']
U2R = [b'buffer_overflow.', b'loadmodule.', b'rootkit.']
R21 = [b'ftp_write.',  b'guess_passwd.', b'imap.', b'multihop.', b'perl.',b'phf.',b'spy.',b'warezclient.',b'warezmaster.'] 
PROB = [ b'ipsweep.', b'nmap.', b'portsweep.', b'satan.']
NORM = [b'normal.']


KEYS = {"dos":DOS, "u2r":U2R, "r21":R21, "prob":PROB, "norm":NORM}




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



def labels(x:numpy.ndarray, label:Dict[str,List[str]])->numpy.ndarray:
	new = numpy.copy(x)
	for key in label.keys():
		for i in label[key]:
			new[numpy.where(new==i)] = key
	return new



if __name__ == "__main__":

	data = DATASET(data_home="~/Documents/project/sklearn-data")

	print(f"\033[0;35mDataset\033[0m: {data.data.shape}")
	#print(f"\033[0;35mFeatures\033[0m: {data.feature_names}")
	#print(f"\033[0;35mLabels\033[0m: {numpy.unique(data.target)}")

	X = numpy.copy(data.data)
	print(f"\nX : {X.shape}")

	y = numpy.copy(data.target)
	y = labels(y, KEYS)
	print(f"y: {numpy.unique(y)}")

	X_train, y_train, X_test, y_test = split(X, y, 45, 0.33)
	print(f"\nTrain: {X_train.shape} {y_train.shape}")
	print(f"Test: {X_test.shape} {y_test.shape}")
