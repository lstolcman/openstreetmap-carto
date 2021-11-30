@black-route: #444444;
@blue-route: #0766c7;
@green-route: #409716;
@red-route: #e64525;
@yellow-route: #ffe034;


#black_bar {
  [zoom >= 14] {
    line/line-color: @black-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}

#blue_bar {
  [zoom >= 14] {
    line/line-color: @blue-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}

#green_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}

#red_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}

#yellow_bar {
  [zoom >= 14] {
    
    line/line-color: @yellow-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
  }
}

//// 2 ntersecting hiking routes

#red_green_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#red_blue_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#red_yellow_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#red_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @black-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#green_blue_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#green_yellow_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#green_black_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @black-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#blue_yellow_bar {
  [zoom >= 14] {
    line/line-color: @blue-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#blue_black_bar {
  [zoom >= 14] {
    line/line-color: @blue-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @black-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}

#yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @yellow-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 2;
    line2/line-color: @black-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: -2;
  }
}


//// 3 intersecting hiking routes

#red_green_blue_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @blue-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#red_green_yellow_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @yellow-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#red_green_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#red_blue_yellow_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @yellow-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#red_blue_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#red_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#green_blue_yellow_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @yellow-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#green_blue_black_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#green_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}

#blue_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @blue-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 4;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 0;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -4;
  }
}



//// 4 intersecting hiking routes

#red_green_blue_yellow_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 6;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 2;
    line3/line-color: @blue-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -2;
    line4/line-color: @yellow-route;
    line4/line-width: 2.5;
    line4/line-dasharray: 20,5;
    line4/line-offset: -6;
  }
}

#red_green_blue_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 6;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 2;
    line3/line-color: @blue-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -2;
    line4/line-color: @black-route;
    line4/line-width: 2.5;
    line4/line-dasharray: 20,5;
    line4/line-offset: -6;
  }
}

#red_green_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 6;
    line2/line-color: @green-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 2;
    line3/line-color: @yellow-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -2;
    line4/line-color: @black-route;
    line4/line-width: 2.5;
    line4/line-dasharray: 20,5;
    line4/line-offset: -6;
  }
}

#red_blue_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @red-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 6;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 2;
    line3/line-color: @yellow-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -2;
    line4/line-color: @black-route;
    line4/line-width: 2.5;
    line4/line-dasharray: 20,5;
    line4/line-offset: -6;
  }
}

#green_blue_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @green-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 6;
    line2/line-color: @blue-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 2;
    line3/line-color: @yellow-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: -2;
    line4/line-color: @black-route;
    line4/line-width: 2.5;
    line4/line-dasharray: 20,5;
    line4/line-offset: -6;
  }
}


// intersection of 5

#red_green_blue_yellow_black_bar {
  [zoom >= 14] {
    line/line-color: @blue-route;
    line/line-width: 2.5;
    line/line-dasharray: 20,5;
    line/line-offset: 8;
    line2/line-color: @yellow-route;
    line2/line-width: 2.5;
    line2/line-dasharray: 20,5;
    line2/line-offset: 4;
    line3/line-color: @black-route;
    line3/line-width: 2.5;
    line3/line-dasharray: 20,5;
    line3/line-offset: 0;
    line4/line-color: @yellow-route;
    line4/line-width: 2.5;
    line4/line-dasharray: 20,5;
    line4/line-offset: -4;
    line5/line-color: @black-route;
    line5/line-width: 2.5;
    line5/line-dasharray: 20,5;
    line5/line-offset: -8;
  }
}