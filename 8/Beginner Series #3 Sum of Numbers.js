function getSum( a,b )
{
    if (a == b){
        return a;

    } else {
        sumi = 0;
        if (a < b){
            for (let i = a; i <= b; i++) {
                sumi += i;
            }
        }else{
            for (let i = a; i >= b; i--) {
                sumi += i;
            }
        }
        return sumi
    }
}