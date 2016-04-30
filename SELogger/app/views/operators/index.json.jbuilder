json.array!(@operators) do |operator|
  json.extract! operator, :id, :name, :call_sign, :location, :event_id
  json.url operator_url(operator, format: :json)
end
