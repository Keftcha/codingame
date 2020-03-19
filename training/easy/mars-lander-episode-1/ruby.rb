STDOUT.sync = true # DO NOT REMOVE

surface_n = gets.to_i # the number of points used to draw the surface of Mars.
surface_n.times do
    land_x, land_y = gets.split(" ").collect {|x| x.to_i}
end

loop do
    x, y, h_speed, v_speed, fuel, rotate, power = gets.split(" ").collect {|x| x.to_i}
    
    if v_speed < -39
        puts "0 4"
    else
        puts "0 0"
    end
end
