def get_currentlyInfected(reportedCases, multiplier):
    return reportedCases * multiplier

def get_infectionsByRequestedTime(currentlyInfected, timeToElapse):
    factor = int(timeToElapse / 3)
    result = currentlyInfected * pow(2, factor)
    result = int(result)
    return result

def get_severeCasesByRequestedTime(infectionsByRequestedTime):
    severeCasesByRequestedTime = infectionsByRequestedTime * (15 / 100)
    return int(severeCasesByRequestedTime)

def get_hospitalBedsByRequestedTime(severeCasesByRequestedTime, totalHospitalBeds):
    expectedHospitalBeds = int(totalHospitalBeds * (35 / 100))
    hospitalBedsByRequestedTime = expectedHospitalBeds - severeCasesByRequestedTime
    return int(hospitalBedsByRequestedTime)

def get_casesForICUByRequestedTime(infectionsByRequestedTime):
    casesForICUByRequestedTime = infectionsByRequestedTime * (5 / 100)
    return int(casesForICUByRequestedTime)

def get_casesForVentilatorsByRequestedTime(infectionsByRequestedTime):
    casesForVentilatorsByRequestedTime = infectionsByRequestedTime * (2 / 100)
    return int(casesForVentilatorsByRequestedTime)

def get_dollarsInFlight(infectionsByRequestedTime):
    dollarsInFlight = infectionsByRequestedTime * 0.65 * 1.5 * 30
    return round(dollarsInFlight, 2)

def estimator(data):

    periodType = data["periodType"]
    timeToElapse = data["timeToElapse"]
    
    if periodType == 'months':
        timeToElapse = int(data["timeToElapse"]) * 30
    else:
        if periodType == 'weeks':
            timeToElapse = int(data["timeToElapse"]) * 7
    
    impact = {}
    impact.update({"currentlyInfected": get_currentlyInfected(data["reportedCases"], 10)})
    impact.update({"infectionsByRequestedTime": get_infectionsByRequestedTime(impact["currentlyInfected"], timeToElapse)})
    impact.update({"severeCasesByRequestedTime": get_severeCasesByRequestedTime(impact["infectionsByRequestedTime"])})
    impact.update({"hospitalBedsByRequestedTime": get_hospitalBedsByRequestedTime(impact["severeCasesByRequestedTime"], data["totalHospitalBeds"])})
    impact.update({"casesForICUByRequestedTime": get_casesForICUByRequestedTime(impact["infectionsByRequestedTime"])})
    impact.update({"casesForVentilatorsByRequestedTime": get_casesForVentilatorsByRequestedTime(impact["infectionsByRequestedTime"])})
    impact.update({"dollarsInFlight": get_dollarsInFlight(impact["infectionsByRequestedTime"])})
    
    severeImpact = {}
    severeImpact.update({"currentlyInfected": get_currentlyInfected(data["reportedCases"], 50)})
    severeImpact.update({"infectionsByRequestedTime": get_infectionsByRequestedTime(severeImpact["currentlyInfected"], timeToElapse)})
    severeImpact.update({"severeCasesByRequestedTime": get_severeCasesByRequestedTime(severeImpact["infectionsByRequestedTime"])})
    severeImpact.update({"hospitalBedsByRequestedTime": get_hospitalBedsByRequestedTime(severeImpact["severeCasesByRequestedTime"], data["totalHospitalBeds"])})
    severeImpact.update({"casesForICUByRequestedTime": get_casesForICUByRequestedTime(severeImpact["infectionsByRequestedTime"])})
    severeImpact.update({"casesForVentilatorsByRequestedTime": get_casesForVentilatorsByRequestedTime(severeImpact["infectionsByRequestedTime"])})
    severeImpact.update({"dollarsInFlight": get_dollarsInFlight(severeImpact["infectionsByRequestedTime"])})
    
    estimate = {}
    estimate.update({"impact": impact})
    estimate.update({"severeImpact": severeImpact})
    
    estimator = {}
    estimator.update({"data": data, "estimate": estimate})
    
    return estimator
