n = gets.to_i
inputs = gets.split(" ")
nombres = []
for i in 0..(n-1)
  x = inputs[i].to_i
  nombres.push x
end

cost = 0
while nombres.length > 1 do
  p = nombres.delete_at(nombres.find_index(nombres.min))
  g = nombres.delete_at(nombres.find_index(nombres.min))
  nombres.insert(0, p + g)
  cost += nombres[0]
end
puts cost
