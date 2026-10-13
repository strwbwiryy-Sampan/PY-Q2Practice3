from pyscript import document, display

def checkNum(e):
    num_bers= ["1", "4", "2", "8"]


    num1= document.getElementById("num1").value
    name= "Ashington"

    confirm_num = num1 in num_bers

    message = (f'Sorry {name}, your number is not found.' , f'Yay! {name}, your number is found.')

    document.getElementById("output1").innerHTML = message[confirm_num]




