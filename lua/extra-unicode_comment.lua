local function unicode_comment_filter(input, env)
  for cand in input:iter() do
    if utf8.len(cand.text) == 1 and (not cand.comment or cand.comment == "") then
      local code = string.format("[U+%04X]", utf8.codepoint(cand.text))
      yield(Candidate(cand.type, cand.start, cand._end, cand.text, code))
    else
      yield(cand)
    end
  end
end

return unicode_comment_filter
