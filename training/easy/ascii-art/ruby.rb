l = gets.to_i
h = gets.to_i
t = gets.chomp.downcase

h.times do
  row = gets.chomp

  t.each_byte do |n|
    n -= 97
    n = n < 0 || 25 < n ? 26 : n

    print row[n*l..(n+1)*l-1]
  end
  puts
end
