# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20160421023522) do

  create_table "contacts", force: :cascade do |t|
    t.string   "call_sign"
    t.string   "name"
    t.string   "location"
    t.datetime "date_time"
    t.integer  "recieved_report"
    t.integer  "given_report"
    t.string   "state"
    t.string   "mode"
    t.string   "band"
    t.float    "frequency"
    t.integer  "operator_id"
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
  end

  add_index "contacts", ["operator_id"], name: "index_contacts_on_operator_id"

  create_table "events", force: :cascade do |t|
    t.string   "call_sign"
    t.string   "location"
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "operators", force: :cascade do |t|
    t.string   "name"
    t.string   "call_sign"
    t.string   "location"
    t.integer  "event_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_index "operators", ["event_id"], name: "index_operators_on_event_id"

end
