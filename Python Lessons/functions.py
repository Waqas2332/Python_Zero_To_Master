def printing(*args,**kwargs):
    print(*args)
    print(kwargs)

courses = ["Math","Art"]
info = {
    "name":"Waqas",
    "age":23
}
printing(courses,info) #This will output both in args bcz nothing has key/value arguement type

printing(*courses,**info) #These starics will put everything out from lists and dictionary and pass them as single value arguements 
# Implemenetation ==> printing(*courses = "Math","Info", **info = "name":"Waqas","age=23") Thats how it is gonna pass in parameters