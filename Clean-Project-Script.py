'''
Sophia Boss
Digital Production Student at Gnomon School of VFX
12/3/2023

Usage:
Removes unused assets in a given Unreal Engine 5 project.
Reduces project size with two clicks.

'''
import unreal, sys

world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()


def get_static_mesh_actors():
    # Get the list of all actors in the current level
    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    # actors = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_all_level_actors()
 
    # Create an empty list to store static mesh actors
    static_mesh_actors = []
 
    # Check all actors in the level
    for actor in actors:
        # Check if the actor is a static mesh actor
        if isinstance(actor, unreal.StaticMeshActor):
            # If it is, add it to the list
            static_mesh_actors.append(actor)
 
    # Return the list of static mesh actors
    return static_mesh_actors

def select_actors(actor_list):
    unreal.EditorLevelLibrary.set_selected_level_actors(actor_list)

# get staticmesh from staticmeshactors
def get_level_static_meshes():
    actors = get_static_mesh_actors()
    # takes a list of static mesh actors and returns a list of the corresponding static meshes and materials without duplicates in the list. 
    meshes = []
    mats = []

    for actor in actors:
        # print(actor)
        mesh_component = actor.static_mesh_component
        mesh = mesh_component.get_editor_property('StaticMesh')
        mat = mesh_component.get_editor_property('override_materials')
        # print(mat)
        if mesh not in meshes:
            # print(mesh)
            meshes.append(mesh)
        if mat not in mats:
            # print(mat)
            mats.append(mat)
    # print(meshes)

    meshAndMats = [meshes, mats]
    return meshAndMats
    
# Get all the static meshes in the project
def get_all_static_meshes():

    meshes = get_level_static_meshes()[0]
    mymesh = meshes[1]
    all_static_meshes = []
    all_assets =  unreal.EditorAssetLibrary.list_assets("/Game/", True, False)

    #Add them if they are static mesh types
    for item in all_assets:
        try:
            myItem = unreal.EditorAssetLibrary.load_asset(item)
        except:
            continue

        if isinstance(myItem, unreal.StaticMesh):
            all_static_meshes.append(myItem)

    return all_static_meshes

def delete_static_meshes():
    static_meshes = get_level_static_meshes()[0]
    all_static_meshes = get_all_static_meshes()
    
    # Iterate over the list and delete any meshes that are not in the list
    count = 0
    for mesh in all_static_meshes:

        # print( str(mesh))
        if mesh not in static_meshes:
            unreal.EditorAssetLibrary.delete_loaded_asset(mesh)
            print("Deleting:")
            print(mesh)
            
        count+=1

# Get all the mats in the project
def get_all_materials():

    meshes = get_level_static_meshes()[1]
    # mymesh = meshes[1]
    all_mats = []
    all_assets =  unreal.EditorAssetLibrary.list_assets("/Game/", True, False)

    #Add them if they are material types
    for item in all_assets:
        try:
            myItem = unreal.EditorAssetLibrary.load_asset(item)
        except:
            continue

        if isinstance(myItem, unreal.Material):
            all_mats.append(myItem)
            # print(myItem)


    return all_mats

def delete_materials():
    materials = get_level_static_meshes()[1]
    allMats = get_all_materials()
    
    # Iterate over the list and delete any meshes that are not in the list
    count = 0
    for mat in allMats:
        if mat not in materials:
            # unreal.EditorAssetLibrary.delete_loaded_asset(mat)
            print("deleting:")
            print(mat)
        count+=1

print("Script running...")
select_actors(get_static_mesh_actors())
delete_static_meshes()
print("Unused assets have been deleted.")