local function unicode_comment_filter(input, env)
  for cand in input:iter() do
    if utf8.len(cand.text) == 1 and (cand.comment or "") == "" then
      local comment = string.format("[U+%04X]", utf8.codepoint(cand.text))
      local new_cand = Candidate(cand.type, cand.start, cand._end, cand.text, comment)
      new_cand.preedit = cand.preedit
      yield(new_cand)
    else
      yield(cand)
    end
  end
end

return unicode_comment_filter
