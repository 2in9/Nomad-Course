const bodyClass = document.body.classList;
const classLong = "long"
const classShort = "short"

function bgColor() {
    if(window.innerWidth >= 1050){
        bodyClass.add(classLong);
    } else if(window.innerWidth < 800){
        bodyClass.add(classShort);
    } else {
        bodyClass.remove(classLong);
        bodyClass.remove(classShort);
    }
}

bgColor();
window.addEventListener("resize", bgColor);