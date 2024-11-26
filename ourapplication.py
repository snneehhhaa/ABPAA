from flask import Flask, url_for, request, render_template,jsonify
from markupsafe import escape

#test
app=Flask(__name__)

@app.route("/",methods=["GET"])
def Home():
    return render_template("home.html")

@app.route("/",methods=["POST"])
def EmployeeFormSent():
    numberofEmployees=request.form["employees"]
    numberofEmployees = int(numberofEmployees)
    if numberofEmployees>100:
        return render_template("result1.html")
    else:
        return render_template("questionnaire.html")
    

def CO2Emissions():
    counter = 0
    co2Emissions = request.form["co2_emissions"]
    co2Emissions = int(co2Emissions)

    if co2Emissions <=200:
        counter=counter+1
        return counter
    else:
        return counter

def EnergyConsumption():
    counter = 0
    energyConsumption = request.form["energy_consumption"]
    energyConsumption = int(energyConsumption)
    if energyConsumption <=20000:
        counter=counter+1
        return counter
    else:
        return counter
 
def RenewableEnergy():
    counter = 0
    renewableEnergy = request.form["renewable_energy"]
    renewableEnergy = int(renewableEnergy)
    if renewableEnergy<=25:
        counter=counter+1
        return counter
    else:
        return counter
 
def WaterWithdrawal():
    counter = 0
    waterWithdrawal = request.form["water_withdrawal"]
    waterWithdrawal = int(waterWithdrawal)
    if waterWithdrawal <=5000:
        counter=counter+1
        return counter
    else:
        return counter

def HazardousWaster():
    counter = 0
    hazardousWaste = request.form["hazardous_waste"]
    hazardousWaste = int(hazardousWaste)
    if hazardousWaste <=3:
        counter=counter+1
        return counter
    else:
        return counter

def CollectiveBargaining():
    counter = 0
    collectiveBargaining = request.form["collective_bargaining"]
    collectiveBargaining = int(collectiveBargaining)
    if collectiveBargaining <=20:
        return counter
    else:
        counter=counter+1
        return counter

def DiscriminationIncidents():
    counter = 0
    discriminationIncidents = request.form["discrimination_incidents"]
    discriminationIncidents = int(discriminationIncidents)
    if discriminationIncidents<=5:
        counter=counter+1
        return counter
    else:
        return counter

def WomenWorkforce():
    counter = 0
    womanWorkforce = request.form["woman_workforce"]
    womanWorkforce = int(womanWorkforce)
    if womanWorkforce<=30:
        return counter
    else:
        counter=counter+1
        return counter

def SupplierScreening():
    counter = 0
    supplierScreening = request.form["supplier_screening"]
    supplierScreening = int(supplierScreening)
    if supplierScreening<=50:
        return counter
    else:
        counter=counter + 1
        return counter
  
def Training():
    counter = 0
    training = request.form["training"]
    training = int(training)
    if training<=20:
        return counter
    else:
        counter=counter+1
        return counter

@app.route("/result", methods=["POST"])
def Result():
    totalcounter = 0

    totalcounter += CO2Emissions()
    totalcounter += EnergyConsumption()
    totalcounter += RenewableEnergy()
    totalcounter += WaterWithdrawal()
    totalcounter += HazardousWaster()
    totalcounter += CollectiveBargaining()
    totalcounter += DiscriminationIncidents()
    totalcounter += WomenWorkforce()
    totalcounter += SupplierScreening()
    totalcounter += Training()

    if totalcounter >= 8:
        return render_template("goldcertificate.html", score = totalcounter)
    elif totalcounter == 7:
        return render_template("silvercertificate.html", score = totalcounter)
    elif totalcounter == 6:
        return render_template("bronzecertificate.html", score = totalcounter)
    else:
        return render_template("bluecertificate.html", score = totalcounter)

if __name__ == "__main__":
    app.run(debug=True)