# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2022_12_10_152732) do
  create_table "definations", force: :cascade do |t|
    t.text "define"
    t.string "example_statement"
    t.binary "approval_status"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "user_id"
    t.integer "word_id"
    t.index ["user_id"], name: "index_definations_on_user_id"
    t.index ["word_id"], name: "index_definations_on_word_id", unique: true
  end

  create_table "letters", force: :cascade do |t|
    t.string "character"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "first_name"
    t.string "last_name"
    t.integer "role"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "words", force: :cascade do |t|
    t.string "title"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "user_id"
    t.integer "letter_id"
    t.index ["letter_id"], name: "index_words_on_letter_id"
    t.index ["user_id"], name: "index_words_on_user_id"
  end

  add_foreign_key "definations", "users"
  add_foreign_key "definations", "words"
  add_foreign_key "words", "letters"
  add_foreign_key "words", "users"
end