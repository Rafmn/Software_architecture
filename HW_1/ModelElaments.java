public class PoligonalModel {
    private List<Poligon> Poligon;
    private Texture Texture;

    public PoligonalModel() {
        this.Texture = Texture;
    }

}

public class Poligon {
    private Point3D Points;
    public Poligon() {
        this.Points = new Point3D();
    }
}

public class Texture {
    '''...'''
}

public class Flash {
    Point3D Location;
    Angle3D Angle;
    Color Color;
    Float Power;

    public Flash(Point3D Location, Angle3D Angle, Color Color, Float Power) {
    this.Location = Location;
    this.Angle = Angle;
    this.Color = Color;
    this.Power = Power;
}

public class Camera {
    Point3D Location;
    Angle3D Angle;
}

public class Scene {
    int id;
    PoligonalModel Models;
    Flash Flashes;
}



