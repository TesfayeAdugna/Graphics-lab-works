#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;
layout (location = 2) in vec2 texCoord;

out vec3 newColor;
out vec2 outTexCoord;

uniform mat4 transform;

void main(){
    gl_Position = transform * vec4(position.x, position.y, position.z, 1.0);
    newColor = color;
    outTexCoord = vec2(texCoord.x, 1.0 - texCoord.y);
}