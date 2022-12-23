class Word < ApplicationRecord
  include PgSearch::Model

  belongs_to :user
  belongs_to :letter
  has_one :defination

  accepts_nested_attributes_for :defination

  pg_search_scope :search_by_title, against: :title
end
