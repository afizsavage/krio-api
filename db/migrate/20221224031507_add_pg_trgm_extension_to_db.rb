class AddPgTrgmExtensionToDb < ActiveRecord::Migration[7.0]
  def change
    execute 'create extension pg_trgm;'
  end
end
