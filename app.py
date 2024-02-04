from flask import Flask, render_template, request

from prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def car_form():
    if request.method == 'POST':
        car_name = request.form['Car_Name']
        year = int(request.form['Year'])
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        fuel_type = request.form['Fuel_Type']
        seller_type = request.form['Seller_Type']
        transmission = request.form['Transmission']
        owner = int(request.form['Owner'])

        data = {"Car_Name": car_name,
        "Year": year,        
        "Present_Price": present_price,
        "Kms_Driven": kms_driven,
        "Fuel_Type": fuel_type,
        "Seller_Type": seller_type,
        "Transmission": transmission,
        "Owner": owner}
            

        obj = PredictionPipeline()
        prediction = obj.predict_output(data)
        
        return str(prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
