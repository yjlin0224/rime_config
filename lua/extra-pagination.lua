local per_page_size = 10
local pages_limit = 50
local cand_limit = per_page_size * pages_limit

local function make_cand_with_page_num(cand, index, total_size)
  local page_num = math.ceil(index / per_page_size)
  local total_size_str = ""
  if total_size == nil then
    if page_num <= pages_limit then
      total_size_str = string.format("%d+", pages_limit)
    else
      total_size_str = string.format("%d+", math.ceil(index / per_page_size))
    end
  else
    total_size_str = tostring(math.ceil(total_size / per_page_size))
  end
  local comment = ""
  if (cand.comment or "") == "" then
    comment = string.format("(%d/%s)", page_num, total_size_str)
  else
    comment = string.format("%s (%d/%s)", cand.comment, page_num, total_size_str)
  end
  local new_cand = Candidate(cand.type, cand.start, cand._end, cand.text, comment)
  new_cand.preedit = cand.preedit
  return new_cand
end

local function pagination_filter(input, env)
  local candidates = {}
  local index = 0
  for cand in input:iter() do
    if index <= cand_limit then
      table.insert(candidates, cand)
      index = index + 1
      goto continue
    end
    if index == cand_limit + 1 then
      for i, c in ipairs(candidates) do
        if i % per_page_size == 1 then
          local new_cand = make_cand_with_page_num(c, i, nil)
          yield(new_cand)
        else
          yield(c)
        end
      end
      index = index + 1
    end
    if index % per_page_size == 1 then
      local new_cand = make_cand_with_page_num(cand, index, nil)
      yield(new_cand)
    else
      yield(cand)
    end
    index = index + 1
    ::continue::
  end
  if index <= cand_limit then
    local total_size = #candidates
    for i, cand in ipairs(candidates) do
      if i % per_page_size == 1 or i == total_size then
        local new_cand = make_cand_with_page_num(cand, i, total_size)
        yield(new_cand)
      else
        yield(cand)
      end
    end
  end
end

return pagination_filter
