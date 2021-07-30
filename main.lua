-- TestWorld

function love.load()
    font = love.graphics.newFont(17)
    str = "Halo Warld!"
    x = love.graphics.getWidth() / 2
    y = love.graphics.getHeight() / 2
end

function love.update()
    --
end

function love.keypressed(key, scancode, isrepeat)
   if key == "escape" then
      love.event.quit()
      love.quit()
      os.exit()
   end
end

function love.draw()
    love.graphics.setFont(font)
    love.graphics.printf(str, x, y, font:getWidth(str), "center")
end

