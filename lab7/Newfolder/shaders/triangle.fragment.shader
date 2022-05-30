#version 330 core

in vec3 newColor;
in vec2 outTexCoord;

out vec4 outcolor;
uniform sampler2D texSampler;

void main(){
    outcolor = vec4(newColor, 1.0);
    outcolor = texture(texSampler, outTexCoord);
}