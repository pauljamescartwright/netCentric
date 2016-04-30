json.array!(@events) do |event|
  json.extract! event, :id, :call_sign
  json.url event_url(event, format: :json)
end
