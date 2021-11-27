import pickle

class model():
    def __init__(self) -> None:
        self.model_ = None

    def load_model(self):
        self.model_ = pickle.load(open( 'lin_regression', 'rb'))
    
    def predict(self,X):
        if self.model_:
            return self.model_.predict(X)
        else:
            raise Exception('Model is not proper loaded.')

if __name__ == '__main__':
    test = model()
    test.load_model()

    X = [[0.2,0.3,0.4,1,1,9,0,1]]
    print(test.model_.predict(X))
