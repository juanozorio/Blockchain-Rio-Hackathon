'use client'
import CarouselBanner from '../../components/CarouselBanner/CarouselBanner';
import Menu from '../../components/Menu';
import Card from '../../components/Card';
import image from '../../public/image1.jpg'


export default function Home() {
  return (
    
    <>
    <Menu />
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <CarouselBanner />
      <br />
      <Card description={'aloha caption'} title={'title aqui'} imageUrl={image} />
      

    

    </main>
    </>
  );
}