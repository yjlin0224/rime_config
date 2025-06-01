-- https://github.com/rime/librime/issues/993#issuecomment-2834735537

local M = {}

function M.init(env)
  local ctx = env.engine.context

  if ctx:get_option("_horizontal") then
    env.left  = KeyEvent("Up")
    env.right = KeyEvent("Down")
  else
    env.left  = KeyEvent("Left")
    env.right = KeyEvent("Right")
  end

  env.tab        = KeyEvent("Tab")
  env.shift_tab  = KeyEvent("Shift+Tab")

  env.processor = Component.Processor(env.engine, "processor", "navigator")
end

function M.fini(env)
end

function M.func(key, env)
  local ctx = env.engine.context

  if ctx:is_composing() then
    local caret_pos = ctx.caret_pos
    local input_len = #ctx.input

    if ((key:eq(env.left) or key:eq(env.shift_tab)) and caret_pos == 0) or
       ((key:eq(env.right) or key:eq(env.tab)) and caret_pos == input_len) then
      return 1
    end

    return env.processor:process_key_event(key)
  end

  return 2
end

return M
