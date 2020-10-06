"""
    Operators:
    Comparison Query Operators
    $eq: =           Example: db.users.find({age: {$lt : 30}})
    $ne: !=          Example: db.users.find({age: {$ne : 22}})
    $gt: >           Example: db.users.find({age: {$gt : 30}})
    $lt: <           Example: db.users.find({age: {$gt : 30, $lt: 50}})
    $gte: >=         Example: db.users.find({age: {$gte : 30}})
    $lte: <=         Example: db.users.find({age: {$lte : 30}})
    $in: entry       Example: db.users.find({age: {$in : [22, 32]}})
    $nin: not entry  Example: db.users.find({age: {$nin : [22, 32]}})

    Logical Query Operators
    $or:             Example: db.users.find({$or : [{name: "Tom"}, {age: 22}]}),
                              db.users.find({name: "Tom", $or : [{age: 22}, {languages: "german"}]}),
                              db.users.find({$or : [{name: "Tom"}, {age: {$gte:30}}]})
    $and:            Example: db.users.find({$and : [{name: "Tom"}, {age: 32}]})
    $not: one condition
    $nor: list condition

    Array Query Operators
    $all:            Example: db.users.find({languages: {$all : ["english", "french"]}})
    $size:           Example: db.users.find({languages: {$size:2}})
    $elemMatch:      Example: db.grades.find({courses: {$elemMatch: {name: "MongoDB", grade: {$gt: 3}}}})

    Element Query Operators
    $exists: key true or false   Example: db.users.find({company: {$exists:true}})
    $type:           Example: db.users.find({age: {$type:"string"}})
                              db.users.find({age: {$type:"number"}})

    Evaluation Query Operators
    $text: Performs text search.
    $regex:          Example: db.users.find({name: {$regex:"b"}})
"""

"""
    Update Operators

    Field Update Operators
    $currentDate: Sets the value of a field to current date, either as a Date or a Timestamp.
    $inc: Increments the value of the field by the specified amount.
    $min: Only updates the field if the specified value is less than the existing field value.
    $max: Only updates the field if the specified value is greater than the existing field value.
    $mul: Multiplies the value of the field by the specified amount.
    $rename: Renames a field.
    $set: Sets the value of a field in a document.
    $setOnInsert: Sets the value of a field if an update results in an insert of a document.
                  Has no effect on update operations that modify existing documents.
    $unset: Removes the specified field from a document.

    Array Update Operators
    $: Acts as a placeholder to update the first element that matches the query condition.
    $[]: Acts as a placeholder to update all elements in an array for the documents that match the query condition.
    $[<identifier>]: Acts as a placeholder to update all elements that match the arrayFilters condition for the 
                     documents that match the query condition
    $addToSet: Adds elements to an array only if they do not already exist in the set.
    $pop: Removes the first or last item of an array.
    $pull: Removes all array elements that match a specified query.
    $push: Adds an item to an array.
    $pullAll: Removes all matching values from an array.

        Update Operator Modifiers
        $each: Modifies the $push and $addToSet operators to append multiple items for array updates.
        $position: Modifies the $push operator to specify the position in the array to add elements.
        $slice: Modifies the $push operator to limit the size of updated arrays.
        $sort: Modifies the $push operator to reorder documents stored in an array.

    Bitwise Update Operator

    $bit: Performs bitwise AND, OR, and XOR updates of integer values.

"""