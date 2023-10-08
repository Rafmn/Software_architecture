interface IShape {
    void draw();
}

interface ICircle {
    void drawCircle();
}

interface ISquare {
    void drawSquare();
}

interface ITriangle {
    void drawTriangle();
}

class Circle implements ICircle{
    void drawCircle(){
    //...
    }
}

class Square implements ISquare {
    void drawSquare(){
    //...
    }
}

class Triangle implements ITriangle {
    void drawTriangle(){
    //...
    }
}

class Shape implements IShape {
    void draw(){
    //...
    }
}
