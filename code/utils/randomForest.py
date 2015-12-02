# This file is for random forest

import numpy as np
from sklearn.ensemble import RandomForestClassifier

def randomForest(X_train, X_test, y_train, y_test):
    """ This function returns test_error by using random forest
        
        Parameters
        ----------
        X_train: 2D array
            Training feature data set
        X_test: 2D array
            Test feature data set
        y_train: 1D array
            Training response variable
        y_test: 1D array
            Test response variable
        
        Returns
        -------
        test_error: float
            test error
        
        """
        clf = RandomForestClassifier()
        clf = clf.fit(X_train, y_train)
        predicted = clf.predict(X_test)
        test_error = 1 - np.mean(y_test == predicted)
                            
        return test_error