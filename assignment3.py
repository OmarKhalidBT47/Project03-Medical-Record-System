#Omar Khalid Rashid Essa Al Thani GCIS.123.603 

class Physician:
  __slots__ = ["_id", "_name", "_specialty"]

  def __init__(self, id, name, specialty):
    self._id = id
    self._name = name
    self._specialty = specialty

  def get_id(self):
    return self._id
  
  def get_name(self):
    return self._name
  
  def get_specialty(self):
    return self._specialty

  def set_id(self, id):
    self._id = id

  def set_name(self, name):
    self._name = name

  def set_specialty(self, specialty):
    self._specialty = specialty

  def __str__(self):
    return f"Physician: ID: {self._id}, Name: {self._name}, Specialty: {self._specialty}"

  def __repr__(self):
    return f"Physician({self._id}, {self._name}, {self._specialty})"


class Patient:
  __slots__ = ["_emr_id", "_name", "_gender", "_phone_number"]

  def __init__(self, emr_id, name, gender, phone_number):
    self._emr_id = emr_id
    self._name = name
    self._gender = gender
    self._phone_number = phone_number

  def get_emr_id(self):
    return self._emr_id

  def get_name(self):
    return self._name

  def get_gender(self):
    return self._gender

  def get_phone_number(self):
    return self._phone_number

  def set_emr_id(self, emr_id):
    self._emr_id = emr_id

  def set_name(self, name):
    self._name = name

  def set_gender(self, gender):
    self._gender = gender

  def set_phone_number(self, phone_number):
    self._phone_number = phone_number

  def __str__(self):
    return f"Patient: EMR_ID: {self._emr_id}, Name: {self._name}, Gender: {self._gender}, Phone: {self._phone_number}"

  def __repr__(self):
    return f"Patient({self._emr_id}, {self._name}, {self._gender}, {self._phone_number})"


class Encounter:
  __slots__ = ["physician", "patient", "date", "disease", "medication"]

  def __init__(self, physician, patient, date, disease, medication):
    self.physician = physician
    self.patient = patient
    self.date = date
    self.disease = disease
    self.medication = medication

  def __str__(self):
    return f"Encounter: Patient: {self.patient.get_name()}, Physician: {self.physician.get_name()}, Date: {self.date}, Disease: {self.disease}, Medication: {self.medication}"


patients = []
physicians = []
encounters = []

with open("patients.csv", "r") as f:
  lines = f.readlines()

for line in lines:
  emr_id, name, gender, phone_number = line.strip().split(",")
  patients.append(Patient(emr_id, name, gender, phone_number))

with open("physicians.csv", "r") as f:
  lines = f.readlines()

for line in lines:
  id, name, specialty = line.strip().split(",")
  physicians.append(Physician(id, name, specialty))

for patient in patients[:5]:
  encounters.append(Encounter(physicians[2], patient, "5/12/2021", "Coronavirus", "citalopram"))


for patient in patients:
  print(patient)

for physician in physicians:
  print(physician)

with open("encounters.csv", "w") as f:
  for encounter in encounters:
    print(encounter)
    f.write(f"{encounter.patient.get_name()},{encounter.physician.get_name()},{encounter.date},{encounter.disease},{encounter.medication}\n")



