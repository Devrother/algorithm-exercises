function perimeter(n) {
    let result = 4;
    let w = 1, h = 1;
    for (let i = 1; i < n+1; i++) {
        if (i % 2 != 0) {
            w += h;
            result += h*4;
        } else {
            h += w;
            result += 4*w; 
        }
    }
    return result;
}