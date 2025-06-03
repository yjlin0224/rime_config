function utf8.sub(s, i, j)
  i = utf8.offset(s, i)
  j = utf8.offset(s, j + 1) - 1
  return string.sub(s, i, j)
end

local function separate_comment_filter(input, env)
  for cand in input:iter() do
    if (cand.comment or "") ~= "" then
      local len = utf8.len(cand.comment)
      if len >= 6 and utf8.sub(cand.comment, 1, 4) == "[CC:" and utf8.sub(cand.comment, len, len) == "]" then
        local comment = utf8.sub(cand.comment, 5, len - 1)
        if utf8.len(cand.text) == utf8.len(comment) then
          local text_cand = Candidate(cand.type, cand.start, cand._end, cand.text, "")
          text_cand.preedit = cand.preedit
          yield(text_cand)
          local cmnt_cand = Candidate(cand.type, cand.start, cand._end, comment, "[简]")
          cmnt_cand.preedit = cand.preedit
          yield(cmnt_cand)
        else
          yield(cand)
        end
      else
        yield(cand)
      end
    else
      yield(cand)
    end
  end
end

return separate_comment_filter
