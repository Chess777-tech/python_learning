class Person:
    
    def __init__(self, fname, mname, lname, age):
        self.fname = fname
        self.mname  = mname
        self.lname  = lname 
        self.age = age 

    def get_full_name(self) -> str:
        full_name = f"{self.fname} {self.mname} {self.lname}"
        return full_name.title()

    def greet_person(self):
        msg = f"Hello, {self.fname.title()}"
        print(msg)


if __name__ == "__main__":
    first_name = "colby"
    middle_name = "maclane"
    last_name = "hessifer"
    age = 22

    person = Person(first_name, middle_name, last_name, age)
    print(f"Person: {person.get_full_name}")
    print(f"Person's Age: {person.age}")
    person.greet_person()