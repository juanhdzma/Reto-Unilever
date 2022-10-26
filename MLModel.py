from sklearn.linear_model import LinearRegression

def getRegression(x,y, wantedX):
    line_fitter = LinearRegression()
    line_fitter.fit(x,y)
    predict = line_fitter.predict(wantedX)
    return predict