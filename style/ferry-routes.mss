@ferry-route: #66f;
@ferry-route-text: @ferry-route;

#ferry-routes {
  [zoom >= 8] {
    /* background prevents problems with overlapping ferry-routes, see #457 */
    background/line-color: @water-color;
    background/line-width: 1; /* Needs to be a bit wider than the route itself because of antialiasing */
    line-color: @ferry-route;
    line-width: 0.4;
    line-dasharray: 4,4;
    [zoom >= 11] {
      background/line-width: 1;
      line-width: 0.8;
      line-dasharray: 6,6;
    }
  }
}

#ferry-routes-text {
  [zoom >= 13] {
    text-name: "[name]";
    text-face-name: @book-fonts;
    text-placement: line;
    text-fill: @ferry-route-text;
    text-spacing: 1000;
    text-size: 10;
    text-dy: -8;
  }
}


#rrr {
  [zoom >= 14] {
    line/line-color: #e64525;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}
#yyy {
  [zoom >= 14] {
    
    line/line-color: #ffe034;

    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-join: round;
        line/line-cap: round;
  }
}


#bbb {
  [zoom >= 14] {
    
    line/line-color: #444444;

    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}


#lll {
  [zoom >= 14] {
    
    line/line-color: #0766c7;

    line/line-width: 2.5;
    line/line-dasharray: 16,6;
    line/line-join: round;
        line/line-cap: round;
  }
}



#ggg {
  [zoom >= 14] {
    
    line/line-color: #409716;

    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-join: round;
        line/line-cap: round;
  }
}

