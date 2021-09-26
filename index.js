
OniChan();
async function OniChan(){
    const response = await fetch('./Images/onichan.jpg');
    const blob = await response.blob();
    document.getElementById('onichan').src = URL.createObjectURL(blob);
}
